# Clean Architecture Python

## TOC

- [Software Architecture](#software-architecture)
  - [Analogy](#analogy)
- [Clean Architecture](#clean-architecture)
  - [Layers and Data Flow](#layers-and-data-flow)
  - [Main Layers](#main-layers)
- [Test Driven Development](#test-driven-development)

### Software Architecture

An architecture can have multiple granularities, which are the “zoom level” we use to look at the components and their connections. The first level is the one that describes the whole process as a black box with inputs and outputs. At this level we are not even concerned with components, we don’t know what’s inside the system and how it works. We only know what it does.

As you zoom in, you start discovering the details of the architecture, that is, which components are in the aforementioned black box and how they are connected. These components are in turn black boxes, and you don’t want to know specifically how they work, but you want to know what their input and outputs are, where the inputs come from, and how the outputs are used by other components.

#### Analogy

Let's consider a Shop. First we will start from higher level (top-level), we will call it zero level and then we will zoom more and dive into further.

- **Zero Level** - A shop, as a black box, is a place where people enter with money and exit with items. The input of the system are people and their money, and the outputs are the same people and items.

  ![Zero Level](./images/zero-level.jpg)

- **Zoom In** - The shop itself needs to buy what it sells first, so another input is represented by the stock the shop buys from the wholesaler and another output by the money it pays for them. At this level the internal structure of the shop is unknown, we don’t even know what it sells. We can however already devise a simple performance analysis, for example comparing the amount of money that goes out (to pay the wholesaler) and the amount of money that comes in (from the customers). If the former is higher than the latter the business is not profitable.

  ![First Level](./images/first-level.jpg)

- **More Zoom In** - Even in the case of a shop that has positive results we might want to increase its performances, and to do this chances are that we need to understand its internal structure and what we can change to increase its productivity. This may reveal, for example, that the shop has too many workers, that are underemployed waiting for clients because we overestimated the size of the business. Or it might show that the time taken to serve is too long and many clients walk away without buying anything. Or maybe there are not enough shelves to display goods and the staff carries stock around all day searching for display space so the shop is in chaos and clients cannot find what they need.

  At this level, however, workers are pure entities, and still we don’t know much about the shop. To better understand the reasons behind a problem we might need to increase the zoom level and look at the workers for what they are, human beings, and start understanding what their needs are and how to help them work better.

### Clean Architecture

The clean architecture is the opposite of spaghetti code, where everything is interlaced and there are no single elements that can be easily detached from the rest and replaced without the whole system collapsing. The main point of the clean architecture is to make clear “what is where and why”, and this should be your first concern while you design and implement a software system, whatever architecture or development methodology you want to follow.

#### Layers and Data Flow

- the communications between elements that live in the samme layer is unrestricted.
- when you want to communciate with other layers you have to foloow one simple roule.

**THE RULE** - _Talk inwards with simple structures, talk outwards through interfaces_.

Your elements should talk outwards using **interfaces**. using only the **expected API** of a component, w/o referring to a **speicific implementation**.

When an **outer layer** is cretaed, elements living there will **plug themselves** into those **interfaces** and provide a **practical implementation**.

#### Main Layers

##### Entities

Domain models, these models are different then framework models like django. these models are not connected with a storage system, so they cant be directly saved or queried using methods of their classes, they dont contain methods to dump as JSON strings, they are not connected with any presetnation layer, they are **lightweight models**.

The architecture allows them to interact directly. This means that one of your python classes can use another one directly, instantiating it and calling it's methdos.

Entitites dont know anything about outer layers like external interfaces, they only work with interfaces.

#### use cases

Use cases implemented by the system. use cases are the processes that happen ino your appication, where you use you domain models to work on real data. Examples can be a user logging in, a search with specific filters being performed, or a bank transaction happening when the user wants to buy the content of the cart.

a use case should be as simple as it can. if we can isolate the system based on its use case then we can test, understand and maintain it more easily.

Use cases know the entities, so they can instantitate them directly and use them. they can also call each other, and it is common to create complex use cases that put together other simpler ones.

#### External systems

External systems that implemetns the interfaces defined in the previous layer. example - a specific framework that exposes an HTTP API, or a specific database.

### APIs and shades of grey

Every layer must be accessed by api defined by inner layer. that is a fixed collection of entry points (methods and objects).

**When desingning an architecture it is very imporatnt to know 'what is where and why', and is even more important when you 'bend' the rules.**

### Test Driven Development

1. Write Tests First, Code Letter
2. Add the reasonably amount of code you need to pass the tests
3. You Shouldn't have more than one failing test
4. Write code that passes the test and refactor it
5. A test should fail the first time you run it. If it doesn’t, ask yourself why you are adding it.
6. Never refactor w/o tests.

#### How many assertions

If the test is a logical `AND` between conditions - then go for multiple assertions.
Or a logical `OR` - Multiple Test functions.

#### How to Fix Bugs

From the TDD point of view, if you don’t have a failing test there is no bug, so you have to come up with at least one test that exposes the issue you are trying to solve.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- python3
- pip3
- virtualenvwrapper

Install `python3`

```bash
sudo apt-get install -y python3
```

Install `pip3`

```bash
sudo apt-get install -y python3-pip
```

Install `virtualenvwrapper`

```bash
sudo pip3 install vitualenvwrapper
```

On your `.zshrc` or `.bashrc`

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
source /usr/local/bin/virtualenvwrapper.sh
```

```bash
source ~/.bashrc
#or
source ~/.zshrc
```

### Installing

Create a virtualenv

```bash
export PROJECT_NAME='clean-architecture-python'
mkvirtualenv $PROJECT_NAME
workon $PROJECT_NAME
```

Clone the Repo

```bash
git clone https://github.com/alamin-mahamud/clean-architecture-python $PROJECT_NAME
cd $PROJECT_NAME
```

Install the requirements

```bash
pip install -r requirements.txt
```

## Running the tests

```bash
pytest -ra
```

## Deployment

Additional notes about how to deploy this on a live system

## Built With

- [pytest](https://docs.pytest.org/en/latest/index.html) - used for tests

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Alamin Mahamud** - _Initial work_ - [alamin-mahamud](https://github.com/alamin-mahamud)
- **Leonardo Giordani** - _Clean Architecture Python_ - [The Digital Cat](http://thedigitalcatonline.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
