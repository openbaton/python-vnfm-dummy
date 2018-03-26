  <img src="https://raw.githubusercontent.com/openbaton/openbaton.github.io/master/images/openBaton.png" width="250"/>
  
  Copyright © 2015-2016 [Open Baton](http://openbaton.org). 
  Licensed under [Apache v2 License](http://www.apache.org/licenses/LICENSE-2.0).

# Python Vnfm Dummy
A dummy Vnfm written in python to be used as example of how to use the Python SDK

## Technical Requirements
This section covers the requirements that must be met by the Python Vnfm Dummy in order to satisfy the demands for such a component:

* python-vnfm-sdk

## How to install Python Vnfm Dummy

First install the dependencies in your environment by running

```bash
pip install python-vnfm-sdk
```

Second step, let's create a configuration file for the VNFManager that looks like:

```ini
[vnfm]

endpoint_type=RABBIT
type=python
endpoint=python-endpoint
log_path=/var/log/openbaton/
broker_ip=127.0.0.1
autodelete=true
heartbeat=60
exchange=openbaton-exchange

```

where:

| name            |    description                                   |
|-----------------|--------------------------------------------------|
| type            |   The type of the vnfm        |
| endpoint_type   |   must be RABBIT                                 |
| broker_ip       |   Ip of the rabbitmq broker used by the nfvo     |
| username        |   username for the rabbitmq broker used to connect to the manager queue of the nfvo|
| password        |   password for the rabbitmq broker used to connect to the manager queue of the nfvo|
| exchange        |   exchange name used in the rabbitmq broker by the nfvo |
| autodelete      |   true or false in case you want the endpoint queue to have the autodelete property (usually true) |
| heartbeat       |   heartbeat for the rabbitmq connection          |
| log_path        |   path where the logfile will be written        |


See the [sdk documentation](https://pypi.python.org/pypi/python-vnfm-sdk) for more details.

## how to run the dummy vnfm in python
 
Then just clone this repository and within the virtualenv run
 
```bash
python __main__.py
```

## How to extend the Python Vnfm Dummy

This example is a good starting point for creating a Vnfm that has strict dependencies on python libraries

## Issue tracker

Issues and bug reports should be posted to the GitHub Issue Tracker of this project

# What is Open Baton?

OpenBaton is an open source project providing a comprehensive implementation of the ETSI Management and Orchestration (MANO) specification.

Open Baton is a ETSI NFV MANO compliant framework. Open Baton was part of the OpenSDNCore (www.opensdncore.org) project started almost three years ago by Fraunhofer FOKUS with the objective of providing a compliant implementation of the ETSI NFV specification. 

Open Baton is easily extensible. It integrates with OpenStack, and provides a plugin mechanism for supporting additional VIM types. It supports Network Service management either using a generic VNFM or interoperating with VNF-specific VNFM. It uses different mechanisms (REST or PUB/SUB) for interoperating with the VNFMs. It integrates with additional components for the runtime management of a Network Service. For instance, it provides autoscaling and fault management based on monitoring information coming from the the monitoring system available at the NFVI level.

## Source Code and documentation

The Source Code of the other Open Baton projects can be found [here][openbaton-github] and the documentation can be found [here][openbaton-doc] .

## News and Website

Check the [Open Baton Website][openbaton]
Follow us on Twitter @[openbaton][openbaton-twitter].

## Licensing and distribution
Copyright [2015-2016] Open Baton project

Licensed under the Apache License, Version 2.0 (the "License");

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Support
The Open Baton project provides community support through the Open Baton Public Mailing List and through StackOverflow using the tags openbaton.

## Supported by
  <img src="https://raw.githubusercontent.com/openbaton/openbaton.github.io/master/images/fokus.png" width="250"/><img src="https://raw.githubusercontent.com/openbaton/openbaton.github.io/master/images/tu.png" width="150"/>

[fokus-logo]: https://raw.githubusercontent.com/openbaton/openbaton.github.io/master/images/fokus.png
[openbaton]: http://openbaton.org
[openbaton-doc]: http://openbaton.org/documentation
[openbaton-github]: http://github.org/openbaton
[openbaton-logo]: https://raw.githubusercontent.com/openbaton/openbaton.github.io/master/images/openBaton.png
[openbaton-mail]: mailto:users@openbaton.org
[openbaton-twitter]: https://twitter.com/openbaton
[tub-logo]: https://raw.githubusercontent.com/openbaton/openbaton.github.io/master/images/tu.png
