#!/usr/bin/env node

'use strict';

const isScoped = require(`is-scoped`);
const pkg = require(`../package.json`);
const program = require(`commander`);
const deployGitTag = require(`../`);
const readPkg = require(`read-pkg`);

program
  .description(pkg.description)
  .version(pkg.version)
  .option(`-a, --access <access>`, `published as [public] or [restricted]`, /^(public|restricted)$/i, `restricted`)
  .option(`-s, --skip-token`, `skip the authentication step`)
  .parse(process.argv);

readPkg()
  .then(pkg => isScoped(pkg.name))

  // You can not restrict an un-scoped package as all un-scoped packages must be published publicly.
  .then(scoped => deployGitTag({ access: scoped ? program.access : `public`, skipToken: program.skipToken }))
  .catch(error => {
    console.error(`npm-publish-git-tag failed for the following reason - ${error}`);
    process.exit(1);
  });
