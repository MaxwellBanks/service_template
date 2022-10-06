# Service Template

This repository provides a simple template and demonstration for a microservice. The demo service here could be considered analagous to a backend service that runs some calculations--something requests a result by calling an endpoint and the service sends back a response.

# Template Components

## API

The provided API is a mvp produced with flask. `routes.py` manages the API endpoints, and `handlers.py` manages the internal logic of the service. Naturally this could be expanded in complexity, but do keep in mind that if the expansion results in scope creep the service should probably be split in two. Much like a function, a microservice should do one thing and do it well.

## Tests

Provided in the tests folder are unit tests and integration tests. If this was a larger scale template with dependencies functional tests would be included, but at this scale function tests would be identical to integration tests. Of additional note is the mocking in `test_routes.py` to allow for unit tests--this is an example of how to unit test something with external dependencies.

## Containerization

This template provides an example dockerfile that can be used to build a container image for this service. This container image can be pushed up to a repository for easy access in production.

## CI/CD

Using Github Actions under `.github/workflows`, a basic CI/CD pipeline has been implemented. At the current time, `pull_request.yml` is identical to `push.yml` in every way except their trigger, resulting in duplicate actions--the point here is to demonstrate that they could be used differently. This will also eventually be refactored to provide better code reuse and auto build/publish the aforementioned Docker container.