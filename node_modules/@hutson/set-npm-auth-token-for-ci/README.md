# @hutson/set-npm-auth-token-for-ci

> Set authentication token placeholder into `.npmrc` file for use in automated CI processes.

## Table of Contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Installation](#installation)
- [Usage](#usage)
- [Debugging](#debugging)
- [Node Support Policy](#node-support-policy)
- [Contributing](#contributing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

To install the `set-npm-auth-token-for-ci` tool for use in your project please run the following command:

```bash
yarn [global] add [--dev] @hutson/set-npm-auth-token-for-ci
```

> **Note:** Whether you install the package globally, as a runtime dependency, or a development dependency, depends on how you plan to use this package. If you are planning to use the CLI from this package to set auth tokens for multiple projects, consider a global installation. Otherwise, consider adding this package as a dependency on the project for which it will be used.

## Usage

When you need to authenticate with an npm-compatible package registry using the `npm` or `yarn` package manager, and you are authenticating with that registry from within a Continuous Integration environment, you are strongly encouraged to use an [authentication token placeholder](http://blog.npmjs.org/post/118393368555/deploying-with-npm-private-modules).

For example, your package may have an [.npmrc file](https://docs.npmjs.com/files/npmrc) that configures a private registry:

```yaml
registry=https://registry.example.com/
```

To authenticate you could set an authentication token in the `.npmrc` file:

```yaml
//registry.example.com/:_authToken=SECRET
```

Now every authenticated request to `registry.example.com/` will receive the `SECRET` token.

However, you may not want to commit your authentication token to your source repository where other people will have access to the token.

Instead, you can inject your token into your Continuous Integration environment using an environment variable, and then configure `npm` and `yarn` to get the authentication token from the environment.

That's where `set-npm-auth-token-for-ci` helps. `set-npm-auth-token-for-ci` gets the registry used by the current package and writes an authentication token placeholder to the correct `.npmrc` file.

If there's an `.npmrc` file located within the current directory, and that directory contains an `package.json` file, then `set-npm-auth-token-for-ci` will write the authentication token placeholder into that `.npmrc` file. Otherwise the authentication token placeholder will be written into the `.npmrc` file located at the root of the user's home directory.

The placeholder is of the form: `[REGISTRY]/:_authToken=${NPM_TOKEN}`

For example, if the package is configured to use our example npm registry, the placeholder will be: `//registry.example.com/:_authToken=${NPM_TOKEN}`

When `npm` or `yarn` need to authenticate, they retrieve the value assigned to `_authToken`, which is `${NPM_TOKEN}`, and then replace `${NPM_TOKEN}` with the value of the `NPM_TOKEN` environment variable.

**CLI Tool**

After you've installed `set-npm-auth-token-for-ci`, you can call the tool based on whether you installed it globally or locally:

_Globally_
```bash
set-npm-auth-token-for-ci
```

_Locally_
```bash
$(yarn bin)/set-npm-auth-token-for-ci
```

**Programmatically**

```javascript
const setNpmAuthTokenForCI = require(`@hutson/set-npm-auth-token-for-ci`);

// To write the authentication token placeholder, invoke the imported function:
setNpmAuthTokenForCI();
```

If an issue is encountered while writing to the `.npmrc` file, an exception will be thrown. Consider wrapping `setNpmAuthTokenForCI` in a `try`/`catch`.

```javascript
try {
  setNpmAuthTokenForCI();
} catch (error) {
  /* Handle the error. */
}
```

## Debugging

To assist users of `set-npm-auth-token-for-ci` with debugging the behavior of this module we use the [debug](https://www.npmjs.com/package/debug) utility package to print information to the console. To enable debug message printing, the environment variable `DEBUG`, which is the variable used by the `debug` package, must be set to a value configured by the package containing the debug messages to be printed.

To print debug messages on a unix system set the environment variable `DEBUG` with the name of this package prior to executing a tool that invokes this module:

```bash
DEBUG=set-npm-auth-token-for-ci [CONSUMING TOOL]
```

On the Windows command line you may do:

```bash
set DEBUG=set-npm-auth-token-for-ci
[CONSUMING TOOL]
```

If you are using the CLI, it would be:

```bash
DEBUG=set-npm-auth-token-for-ci set-npm-auth-token-for-ci
```

On the Windows command line you may do:

```bash
set DEBUG=set-npm-auth-token-for-ci
set-npm-auth-token-for-ci
```

## Node Support Policy

We only support [Long-Term Support](https://github.com/nodejs/LTS) versions of Node.

We specifically limit our support to LTS versions of Node, not because this package won't work on other versions, but because we have a limited amount of time, and supporting LTS offers the greatest return on that investment.

It's possible this package will work correctly on newer versions of Node. It may even be possible to use this package on older versions of Node, though that's more unlikely as we'll make every effort to take advantage of features available in the oldest LTS version we support.

As each Node LTS version reaches its end-of-life we will remove that version from the `node` `engines` property of our package's `package.json` file. Removing a Node version is considered a breaking change and will entail the publishing of a new major version of this package. We will not accept any requests to support an end-of-life version of Node. Any merge requests or issues supporting an end-of-life version of Node will be closed.

We will accept code that allows this package to run on newer, non-LTS, versions of Node. Furthermore, we will attempt to ensure our own changes work on the latest version of Node. To help in that commitment, our continuous integration setup runs against all LTS versions of Node in addition the most recent Node release; called _current_.

JavaScript package managers should allow you to install this package with any version of Node, with, at most, a warning if your version of Node does not fall within the range specified by our `node` `engines` property. If you encounter issues installing this package, please report the issue to your package manager.

## Contributing

Please read our [contributing guide](https://gitlab.com/hyper-expanse/open-source/set-npm-auth-token-for-ci/blob/master/CONTRIBUTING.md) to see how you may contribute to this project.
