# Parametrik - parametrized svg drawings

## Setup

## Prerequisites
- [Python](https://www.python.org)
- [Docker](https://www.docker.com/)

### How to install for local development

`poetry install`

`poetry shell` - activates virtual environment

### How to start production setup (still with development environment variables)

`docker-compose -f docker-compose.yml up`

### How to start development server and run tests

`docker-compose up`

### Testing

`docker-compose up test`

### QA checks - black, flake8, xenon

`tox`

## Solution decisions

I decided to use dockerized setup for the project. It has separate development service configuration.
For the needs of testing with the dockerized database I also prepared `test` service that uses
the same object as a `web` API service. I also considered database agnostic tests but in this case, 
much of the logic is handled by the database itself.

To deal with geometric objects I decided to use PostGIS and configured it to work with Django 
(following [documentation](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/)). I felt that
this is a right tool for that problem. Database stores geometric objects properly and gives
validations. With this I didn't have to write geometric logic for my own, so that the solution is
less error prone. I was also motivated by PostGIS `AsSVG` annotation that could be used for 
generating SVG images.

During the implementation I realised that the format of SVG output from PostGIS is different 
than example `output.svg` file but I stayed with that tech stach, because the final wasn't
different.

In the code I provided separation between view and core logic. View uses provided services to 
generate projections. There is also a custom serializer that converts and validates user input to the internal
data objects represantation (entities). 

Tests are provided on two stages - integration and unit. Unit tests verifies internal core logic
without touching any external dependencies. On the integration level tests uses django test database
and verifies real projections from given coordinates to database represenataions and finally
svg contents.


## Questions to a domain expert

- I assumed that it is better to store each part of the bookcase as a separate database object.
Because it feels like better option for generating real parametric documents for the factories.
  I also considered storing whole product in a single column field (multipolygon in postgis). 
  What is better in this situation?
  
- 