Objective:
A RESTful App to support users to create new endpoints, post data to that, and access the same.

    For the project sake, we have configured 5 minutes as Expiry for each newly created endpoint.

    Background job by ApScheduler takes care of cleaning up the DB, and deactivating Endpoints.

    Endpoints:
        LIST(GET): /webhook-testing/v1/endpoints
        DETAIL(GET): /webhook-testing/v1/endpoints/{uniqueid}
        CREATE(GET): /webhook-testing/v1/endpoints/create
        POST(POST): /webhook-testing/v1/endpoints/{uniqueid}/post

    CodeCoverage: 60%
Documented by Swagger, and Sphinx.

Hosted on Heroku, Gunicorn
