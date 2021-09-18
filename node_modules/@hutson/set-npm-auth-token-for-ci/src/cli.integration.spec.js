'use strict';

const {expect} = require(`chai`);
const fs = require(`fs`);
const path = require('path');
const {afterEach, beforeEach, describe, it} = require(`mocha`);
const shell = require(`shelljs`);
const tmp = require(`tmp`);

shell.config.silent = true;

describe(`set-npm-auth-token-for-ci CLI`, function () {
  // Setting up our fake project takes longer than the default Mocha timeout.
  this.timeout(20000);

  describe(`when publishing fails`, () => {
    beforeEach(function () {
      this.binPath = path.resolve('src/cli.js');

      // Switch into a temporary directory to isolate the behavior of this tool from
      // the rest of the environment.
      this.cwd = process.cwd();
      this.tmpDir = tmp.dirSync();
      process.chdir(this.tmpDir.name);

      fs.writeFileSync(`.npmrc`, ``);
    });

    afterEach(function () {
      process.chdir(this.cwd);
    });

    it(`returns a non-zero code when the current directory does not contain package.json`, function () {
      const cliResponse = shell.exec(`node ${this.binPath}`);
      expect(cliResponse.code).to.be.a('number').and.to.equal(1);
      expect(cliResponse.stderr).to.have.string(`set-npm-auth-token-for-ci failed for the following reason`);
      expect(cliResponse.stderr).to.have.string(`Error: ENOENT: no such file or directory`);
    });

    /**
     * How do we run this test in a way that prevents this package from writing to a user's
     * home directory is the code is badly broken?
     */
    it.skip(`will set authentication token if not already set`);
  });
});
