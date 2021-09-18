#!/usr/bin/env node

'use strict';

const pkg = require(`../package.json`);
const program = require(`commander`);
const index = require(`./index`);

program
  .description(pkg.description)
  .version(pkg.version)
  .parse(process.argv);

try {
  index();
} catch (error) {
  console.error(`set-npm-auth-token-for-ci failed for the following reason - ${error}`);
  process.exit(1);
}
