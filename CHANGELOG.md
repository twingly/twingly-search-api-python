# Changelog

## [2.1.4](https://github.com/twingly/twingly-search-api-python/tree/2.1.4) (2020-09-07)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/2.1.3...2.1.4)

**Merged pull requests:**

- Insert newline in MANIFEST.in [\#52](https://github.com/twingly/twingly-search-api-python/pull/52) ([Pontus4](https://github.com/Pontus4))
- Run tests on Bionic on Travis CI [\#50](https://github.com/twingly/twingly-search-api-python/pull/50) ([walro](https://github.com/walro))

## [2.1.3](https://github.com/twingly/twingly-search-api-python/tree/2.1.3) (2019-04-08)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/2.1.2...2.1.3)

**Implemented enhancements:**

- Migrate to pypi.org [\#39](https://github.com/twingly/twingly-search-api-python/issues/39)

**Closed issues:**

- Release a new version [\#46](https://github.com/twingly/twingly-search-api-python/issues/46)

**Merged pull requests:**

- Use twine when publishing [\#48](https://github.com/twingly/twingly-search-api-python/pull/48) ([walro](https://github.com/walro))

## [2.1.2](https://github.com/twingly/twingly-search-api-python/tree/2.1.2) (2019-04-05)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/2.1.1...2.1.2)

**Implemented enhancements:**

- Test the install procedure in Windows [\#45](https://github.com/twingly/twingly-search-api-python/issues/45)
- Use pytest instead of Nose [\#43](https://github.com/twingly/twingly-search-api-python/issues/43)

**Merged pull requests:**

- Switch to pytest instead of nose [\#47](https://github.com/twingly/twingly-search-api-python/pull/47) ([walro](https://github.com/walro))
- Test the install procedure [\#42](https://github.com/twingly/twingly-search-api-python/pull/42) ([dentarg](https://github.com/dentarg))
- Add all required modules in setup.py [\#40](https://github.com/twingly/twingly-search-api-python/pull/40) ([sp1thas](https://github.com/sp1thas))

## [2.1.1](https://github.com/twingly/twingly-search-api-python/tree/2.1.1) (2017-10-20)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/2.1.0...2.1.1)

**Implemented enhancements:**

- Add changelog [\#37](https://github.com/twingly/twingly-search-api-python/issues/37)

**Merged pull requests:**

- Do not include TZ information in queries [\#38](https://github.com/twingly/twingly-search-api-python/pull/38) ([walro](https://github.com/walro))

## [2.1.0](https://github.com/twingly/twingly-search-api-python/tree/2.1.0) (2017-06-01)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/2.0.0...2.1.0)

**Implemented enhancements:**

- Coordinates on Post object [\#36](https://github.com/twingly/twingly-search-api-python/issues/36)
- Lacks test for attributes in twinglydata element [\#26](https://github.com/twingly/twingly-search-api-python/issues/26)

**Fixed bugs:**

- Parse post coordinates correctly [\#34](https://github.com/twingly/twingly-search-api-python/issues/34)

**Merged pull requests:**

- Parse coordinates correctly [\#35](https://github.com/twingly/twingly-search-api-python/pull/35) ([roback](https://github.com/roback))

## [2.0.0](https://github.com/twingly/twingly-search-api-python/tree/2.0.0) (2017-05-22)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/1.2.1...2.0.0)

**Closed issues:**

- Update Python client to Search API v3 \[$100\] [\#31](https://github.com/twingly/twingly-search-api-python/issues/31)
- Cannot pip/easy\_install twingly-search: missing README.md [\#30](https://github.com/twingly/twingly-search-api-python/issues/30)

**Merged pull requests:**

- Minor fixes before release [\#33](https://github.com/twingly/twingly-search-api-python/pull/33) ([roback](https://github.com/roback))
- Update Python client to Search API v3 [\#32](https://github.com/twingly/twingly-search-api-python/pull/32) ([xSAVIKx](https://github.com/xSAVIKx))

## [1.2.1](https://github.com/twingly/twingly-search-api-python/tree/1.2.1) (2016-06-21)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/1.2.0...1.2.1)

**Closed issues:**

- Multiple languages throws exception [\#29](https://github.com/twingly/twingly-search-api-python/issues/29)
- SSLError api.twingly.com != tw.ly [\#27](https://github.com/twingly/twingly-search-api-python/issues/27)

**Merged pull requests:**

- Python SNI support is required [\#28](https://github.com/twingly/twingly-search-api-python/pull/28) ([walro](https://github.com/walro))

## [1.2.0](https://github.com/twingly/twingly-search-api-python/tree/1.2.0) (2016-03-03)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/1.0.3...1.2.0)

**Fixed bugs:**

- Instance variables not declared correctly [\#23](https://github.com/twingly/twingly-search-api-python/issues/23)
- No validation on Query\#start\_time and \#end\_time if they are strings [\#22](https://github.com/twingly/twingly-search-api-python/issues/22)
- Tags not returned from parser [\#18](https://github.com/twingly/twingly-search-api-python/issues/18)
- Add tests that actually tests the parser [\#17](https://github.com/twingly/twingly-search-api-python/issues/17)
- Unused methods [\#14](https://github.com/twingly/twingly-search-api-python/issues/14)

**Closed issues:**

- Convert query start and end time to UTC [\#16](https://github.com/twingly/twingly-search-api-python/issues/16)

**Merged pull requests:**

- Make sure Query\#start\_time and \#end\_time are datetimes [\#25](https://github.com/twingly/twingly-search-api-python/pull/25) ([roback](https://github.com/roback))
- Make sure instance variables are declared in \_\_init\_\_ [\#24](https://github.com/twingly/twingly-search-api-python/pull/24) ([roback](https://github.com/roback))
- Convert datetimes to UTC [\#21](https://github.com/twingly/twingly-search-api-python/pull/21) ([roback](https://github.com/roback))
- Parser tests [\#19](https://github.com/twingly/twingly-search-api-python/pull/19) ([roback](https://github.com/roback))
- Fix \#14 - unused methods [\#15](https://github.com/twingly/twingly-search-api-python/pull/15) ([bearburger](https://github.com/bearburger))

## [1.0.3](https://github.com/twingly/twingly-search-api-python/tree/1.0.3) (2016-02-05)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/1.0.2...1.0.3)

**Implemented enhancements:**

- Remove .spec file [\#13](https://github.com/twingly/twingly-search-api-python/issues/13)

**Closed issues:**

- Publish to PyPi [\#9](https://github.com/twingly/twingly-search-api-python/issues/9)

**Merged pull requests:**

- Generate README.rst dynamically [\#12](https://github.com/twingly/twingly-search-api-python/pull/12) ([walro](https://github.com/walro))

## [1.0.2](https://github.com/twingly/twingly-search-api-python/tree/1.0.2) (2016-02-03)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/1.0.1...1.0.2)

**Merged pull requests:**

- Improve the inspect method [\#10](https://github.com/twingly/twingly-search-api-python/pull/10) ([dentarg](https://github.com/dentarg))

## [1.0.1](https://github.com/twingly/twingly-search-api-python/tree/1.0.1) (2016-02-03)

[Full Changelog](https://github.com/twingly/twingly-search-api-python/compare/88ef913a292c0095036c2d2f4c05c6dadbddec8b...1.0.1)

**Implemented enhancements:**

- Update Travis CI settings [\#8](https://github.com/twingly/twingly-search-api-python/issues/8)

**Closed issues:**

- Copy/paste error in tests [\#7](https://github.com/twingly/twingly-search-api-python/issues/7)
- About the inspect method [\#6](https://github.com/twingly/twingly-search-api-python/issues/6)
- Need to set API\_KEY env when running tests [\#5](https://github.com/twingly/twingly-search-api-python/issues/5)
- Test queries real endpoint [\#4](https://github.com/twingly/twingly-search-api-python/issues/4)
- Name in twingly.spec [\#3](https://github.com/twingly/twingly-search-api-python/issues/3)
- Can't get the tests to pass [\#2](https://github.com/twingly/twingly-search-api-python/issues/2)
- Missing test dependency? [\#1](https://github.com/twingly/twingly-search-api-python/issues/1)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
