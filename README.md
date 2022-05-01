# InfoITJobs - HackUPC 2022
Hack UPC 2022 Project

![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
![Angular.js](https://img.shields.io/badge/angular.js-%23E23237.svg?style=for-the-badge&logo=angularjs&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Objective
There are tons of jobs in IT and for professionals looking for a position, it may definitely get a bit overwhelming. By relating a huge database of jobs such as Infojobs more directly to prospective applicants, we believe we can provide smooth and efficient experience for both the contractors and the people looking for jobs.

This repository contains:

1. Completed: Given a list with a user's skills, it produces an ordered list of suitable IT jobs obtained from the Infojobs api. Due to inconsistence in the database, this cannot be done, but we can recommend a specific IT job category based on the user's skills, all served on an intuitive and easy to use website.

2. (WIP) The user an input the skills in a multiple select dropdown menu on the frontend.

3. (WIP) The user can search for IT jobs according to relevant criteria, such as experience needed, location, salary and categories.

Standard Readme is designed for open source libraries. Although it’s [historically](#background) made for Node and npm projects, it also applies to libraries in other languages and package managers.


## Table of Contents

- [Background](#background)
- [Install](#install)
- [Development server](#development_server)
- [Code Scaffolding](#badge)
- [Build](#example-readmes)
- [Running unit tests](#related-efforts)
- [Running end-to-end tests](#maintainers)
- [License](#license)

## Background

Standard Readme started with the issue originally posed by [@maxogden](https://github.com/maxogden) over at [feross/standard](https://github.com/feross/standard) in [this issue](https://github.com/feross/standard/issues/141), about whether or not a tool to standardize readmes would be useful. A lot of that discussion ended up in [zcei's standard-readme](https://github.com/zcei/standard-readme/issues/1) repository. While working on maintaining the [IPFS](https://github.com/ipfs) repositories, I needed a way to standardize Readmes across that organization. This specification started as a result of that.

> Your documentation is complete when someone can use your module without ever
having to look at its code. This is very important. This makes it possible for
you to separate your module's documented interface from its internal
implementation (guts). This is good because it means that you are free to
change the module's internals as long as the interface remains the same.

> Remember: the documentation, not the code, defines what a module does.

~ [Ken Williams, Perl Hackers](http://mathforum.org/ken/perl_modules.html#document)

Writing READMEs is way too hard, and keeping them maintained is difficult. By offloading this process - making writing easier, making editing easier, making it clear whether or not an edit is up to spec or not - you can spend less time worrying about whether or not your initial documentation is good, and spend more time writing and using code.

By having a standard, users can spend less time searching for the information they want. They can also build tools to gather search terms from descriptions, to automatically run example code, to check licensing, and so on.

The goals for this repository are:

1. A well defined **specification**. This can be found in the [Spec document](spec.md). It is a constant work in progress; please open issues to discuss changes.
2. **An example README**. This Readme is fully standard-readme compliant, and there are more examples in the `example-readmes` folder.
3. A **linter** that can be used to look at errors in a given Readme. Please refer to the [tracking issue](https://github.com/RichardLitt/standard-readme/issues/5).
4. A **generator** that can be used to quickly scaffold out new READMEs. See [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme).
5. A **compliant badge** for users. See [the badge](#badge).

## Install

This project uses [node](http://nodejs.org) and [npm](https://npmjs.com). Go check them out if you don't have them locally installed.

```sh
$ nvm install v16.13.1
$ nvm use v16.13.1
$ npm install
```

The project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 13.3.4.
Install Angular through [Angular Documentation](https://angular.io/guide/setup-local).

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## License

[MIT](LICENSE) © HackUPC2022
 
