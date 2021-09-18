'use strict';

const Bluebird = require(`bluebird`);
const debug = require(`debug`)(`npm-publish-git-tag`);
const gitLatestSemverTag = Bluebird.promisify(require(`git-latest-semver-tag`));
const readPkg = require(`read-pkg`);
const semver = require(`semver`);
const setNpmAuthTokenForCI = require(`@hutson/set-npm-auth-token-for-ci`);
const shell = require(`shelljs`);
const writePkg = require(`write-pkg`);

module.exports = deployGitTag(shell);
module.exports.deployGitTag = deployGitTag;

function deployGitTag (shell) {
  return options =>
    gitLatestSemverTag()
      .then(latestTag => {
        debug(`latest semver tag retrieved from disk is ${latestTag} `);
        if (semver.valid(latestTag)) {
          return latestTag;
        }
        throw new Error(`No valid semantic version tag available for deploying.`);
      })
      .then(updateVersion)
      .then(() => options.skipToken || setToken())
      .then(() => deploy({ access: options.access }));

  function updateVersion (version) {
    debug(`updating version in package.json to ${version}`);

    return readPkg().then(pkg => writePkg(Object.assign(pkg, { version })));
  }

  function setToken () {
    if (!process.env.NPM_TOKEN) {
      throw new Error(`Cannot find NPM_TOKEN set in your environment.`);
    }
    setNpmAuthTokenForCI();
  }

  function deploy (options) {
    let command = `npm publish`;

    if (typeof options.access === `string`) {
      debug(`publishing package with the following access level`, options.access);
      command += ` --access ${options.access}`;
    }

    debug(`executing publish command - ${command}`);
    const result = shell.exec(command, { silent: true });

    if (result.code !== 0) {
      throw new Error(result.stderr);
    }

    return true;
  }
}
