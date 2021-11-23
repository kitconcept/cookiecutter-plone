from plone.restapi.services import Service


class HelloWorldGet(Service):
    def reply(self):
        return {"message": "hello world"}
