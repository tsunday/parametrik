# Excercise instructions
For this task, you will be required to create a Django project with one endpoint.
It will have to accept:
 - dict describing the geometry
 - string with the plane ('XY', 'YZ', 'XZ')
 
and return :
 - svg file - a drawing based  on the geometry data, projected to plane described in projection_plane
The endpoint's specification is described below:
```yaml
paths:
  /projection:
    post:
      summary: Returns an svg file with a 2d projection.
      produces:
        - image/svg+xml
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Body"
      responses:
        200:
          description: OK
          content:
            image/svg+xml:
              schema:
                type: string
components:
  schemas:
    Body:
      type: object
      properties:
        geometry:
          type: array
          items:
            $ref: "#/components/schemas/Geometry"
        projection_plane:
          type: string
    Geometry:
      type: object
        properties:
          x1: integer
          x2: integer
          y1: integer
          y2: integer
          z1: integer
          z2: integer
```
In the attachment, you can also find a sample geometry json files. \
Remember to test your solution!
# How to send the solution
 - create a new, empty, private repository on GitHub
 - do all of your work on a new branch (or branches), not on master
 - when you're ready, create a new pull request (or pull requests)
 - add @KJagiela, @TomekGancarczyk and @teodormichalski to reviewers
 - wait for our reviews ;)
