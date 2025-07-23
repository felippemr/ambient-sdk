# Changelog

## 0.1.0-alpha.9 (2025-07-23)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Bug Fixes

* **parsing:** parse extra field types ([b153bfb](https://github.com/felippemr/ambient-sdk/commit/b153bfbf64238729686396fdc2cb0cfc7489c99e))

## 0.1.0-alpha.8 (2025-07-22)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* clean up environment call outs ([2086ac7](https://github.com/felippemr/ambient-sdk/commit/2086ac739e360d8223bb44ffd608681e32645790))


### Bug Fixes

* **ci:** correct conditional ([b26c9e9](https://github.com/felippemr/ambient-sdk/commit/b26c9e9f295fd90d2a34ec00d0d53b1291292ce5))
* **ci:** release-doctor — report correct token name ([54f5078](https://github.com/felippemr/ambient-sdk/commit/54f5078480683657031446033ae3135125a52a4c))
* **client:** don't send Content-Type header on GET requests ([df85fcc](https://github.com/felippemr/ambient-sdk/commit/df85fcc56f084779639db80e588b8883c8a1426a))
* **parsing:** correctly handle nested discriminated unions ([8a57059](https://github.com/felippemr/ambient-sdk/commit/8a570596ff30b5f24bf4a95bade6ad1aba1f38a8))
* **parsing:** ignore empty metadata ([77ac3fe](https://github.com/felippemr/ambient-sdk/commit/77ac3fe8607ce71a7b884e44183ee84856d897f4))


### Chores

* **ci:** change upload type ([0d3c998](https://github.com/felippemr/ambient-sdk/commit/0d3c9980ff9f140c9ccfcfb7c058a5d745f4a356))
* **ci:** only run for pushes and fork pull requests ([b7f1468](https://github.com/felippemr/ambient-sdk/commit/b7f1468f5d045d8ff33e3011f267159f757f620f))
* **internal:** bump pinned h11 dep ([5b8f522](https://github.com/felippemr/ambient-sdk/commit/5b8f522241042547ad87acd035505412c3f403ad))
* **internal:** codegen related update ([0c48508](https://github.com/felippemr/ambient-sdk/commit/0c485084cc798b8e3a0db405fd4dac0021a5a894))
* **package:** mark python 3.13 as supported ([1672838](https://github.com/felippemr/ambient-sdk/commit/167283850a727cba776c88d23483ae6c61ef3ae6))
* **readme:** fix version rendering on pypi ([bfa7e82](https://github.com/felippemr/ambient-sdk/commit/bfa7e82a17a612026ea5fdf9a0653775ce878aa9))

## 0.1.0-alpha.7 (2025-06-24)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **client:** add support for aiohttp ([bc2e79b](https://github.com/felippemr/ambient-sdk/commit/bc2e79bc36c05d4b2f55114dda85be92f5c4b9dc))


### Chores

* **tests:** skip some failing tests on the latest python versions ([30f0a9c](https://github.com/felippemr/ambient-sdk/commit/30f0a9cad32441e5fd922c05c09fe88bf3c1b5ca))

## 0.1.0-alpha.6 (2025-06-19)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Documentation

* **client:** fix httpx.Timeout documentation reference ([ba2a81e](https://github.com/felippemr/ambient-sdk/commit/ba2a81e622029edf841715252e38aa942ed318da))

## 0.1.0-alpha.5 (2025-06-18)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([de8a4ab](https://github.com/felippemr/ambient-sdk/commit/de8a4ab1a86782c1d3ae5cb0705b22e24ecff158))


### Chores

* **readme:** update badges ([aa8679b](https://github.com/felippemr/ambient-sdk/commit/aa8679b9fbb0086b7d03ee2abcfc22950f310239))

## 0.1.0-alpha.4 (2025-06-17)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Bug Fixes

* **client:** correctly parse binary response | stream ([6262c8d](https://github.com/felippemr/ambient-sdk/commit/6262c8dd74d3ad17eecc6c76e0690ecd23753e90))


### Chores

* **ci:** enable for pull requests ([2c38138](https://github.com/felippemr/ambient-sdk/commit/2c38138a0b6189e83f9d4bed3b8b62feefc16dc2))
* **internal:** update conftest.py ([47a6d3a](https://github.com/felippemr/ambient-sdk/commit/47a6d3a202bcbdf832c59264786698ec83d54326))
* **tests:** add tests for httpx client instantiation & proxies ([064fa35](https://github.com/felippemr/ambient-sdk/commit/064fa35859c649d3ce303dbd32dd136434667014))
* **tests:** run tests in parallel ([7330626](https://github.com/felippemr/ambient-sdk/commit/73306269414193a7379ac987eaf853053547e0ff))

## 0.1.0-alpha.3 (2025-06-03)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **client:** add follow_redirects request option ([423d841](https://github.com/felippemr/ambient-sdk/commit/423d84195de33483c06dd527e9b1bbecddc201db))


### Chores

* **docs:** remove reference to rye shell ([ae8316c](https://github.com/felippemr/ambient-sdk/commit/ae8316cdc8f9b8328f59f20213e2d4c1efaf14cf))

## 0.1.0-alpha.2 (2025-05-27)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/felippemr/ambient-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([b7e63fa](https://github.com/felippemr/ambient-sdk/commit/b7e63fade019c892a7223b2ab2583f6768f06171))
* **api:** update via SDK Studio ([d96b413](https://github.com/felippemr/ambient-sdk/commit/d96b413df36ab632481238a62fd14610a06f1746))

## 0.1.0-alpha.1 (2025-05-22)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/felippemr/ambient-sdk/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([e9ee898](https://github.com/felippemr/ambient-sdk/commit/e9ee898b191af6018ba15c87f80eb5dda756cd32))


### Chores

* **ci:** fix installation instructions ([54b975c](https://github.com/felippemr/ambient-sdk/commit/54b975cc1614ae4b2418847e0127088bdc153976))
* **ci:** upload sdks to package manager ([a9248c3](https://github.com/felippemr/ambient-sdk/commit/a9248c315a3560a394afa80e6458abb1870d8ab5))
* **docs:** grammar improvements ([14ba4a8](https://github.com/felippemr/ambient-sdk/commit/14ba4a844b3f8d6c17c80ede2a1f728fc1e1cbf6))
* **internal:** codegen related update ([32b227b](https://github.com/felippemr/ambient-sdk/commit/32b227bf7c45d7a02b4b74ccc00776b6fad09c88))

## 0.0.1-alpha.1 (2025-05-12)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/felippemr/ambient-sdk/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* update SDK settings ([925beab](https://github.com/felippemr/ambient-sdk/commit/925beabb2c45117223fb83e9841a011b32ceeae5))
* update SDK settings ([0040034](https://github.com/felippemr/ambient-sdk/commit/0040034caffb66faf48ac23fa3a85c48d2cd54f7))
