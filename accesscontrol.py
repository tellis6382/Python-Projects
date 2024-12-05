class Grade:
  def on_get(self, req, resp):
      grade = lookup_grade(req.params["subjectID"], req.params
      ["studentID"]
      resp.media = grade
app = falcon.App{}
app.add_route("/grades", Grade())
