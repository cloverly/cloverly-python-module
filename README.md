# Cloverly Python Module
[![PyPI version](https://badge.fury.io/py/cloverly-python-module.svg)](https://badge.fury.io/py/cloverly-python-module)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The [Cloverly API](https://www.cloverly.com/carbon-offset-documentation "Cloverly API") Python module

Usage
------
### Requirements
You should be signed up on the [Cloverly Dashboard](https://dashboard.cloverly.com/user/new)  so that you can create and manage cloverly resources.
### Installation
To easily install or upgrade to the latest release, use [pip](http://www.pip-installer.org/).
```bash
pip3 install --upgrade cloverly-python-module
```
<details>
<summary><b>Table of Contents</b> (click to open)</summary>
<!-- MarkdownTOC -->

1. [Getting started](#getting-started)
2. [Resources](#resources)
3. [API Versioning](#api-versioning)
4. [Limitations](#limitations)

<!-- /MarkdownTOC -->
</details>

### Getting Started <a name="getting-started"></a>
1. Log in to your cloverly dashboard and grab your **public** API key.
2. Set up a cloverly session using `clover.CloverlyResource.activate_session` like so:
```python
import cloverly

cloverly.CloverlyResource.activate_session(api_key=API_KEY, version=API_VERSION)
```
3. Now you can perform any resource actions as needed in an authenticated section
4. It's generally best practice to clear your session once you're done like so:
```python
cloverly.CloverlyResource.clear_session()
```

### Resources <a name="resources"></a>
As of 06/08/2021, there are 4 key resource classes:
  - [Estimate](#estimate)
  - [Offset](#offset)
  - [Offset Type](#offset-type)
  - [Purchase](#purchase)

The resource classes are what allow you to create, update, delete and list resource endpoints. Resources also implement subpoints in accordance with [Cloverly's API documentation](https://www.cloverly.com/carbon-offset-documentation). For example, the /estimates/shipping endpoint can be accessed via the Shipping sub class:
```python
cloverly.Estimate.Shipping(from={"zip":"35209"}, to={"zip":"94043"})
```
The above code snippet would return an instance of the Estimate class. All attributes returned in the expected payload would be able to be accessed as instance attributes, like `estimate.slug`

### API Versioning <a name="api-versioning"></a>
Versioning of the API can be passed to the python module in the session activation. Essentially, this populates the following in an API url:
```
https://api.cloverly.com/VERSION_HERE/estimates
```
### Limitations <a name="limitations"></a>
Currently there is no support for:
- asynchronous requests
- persistent connections
