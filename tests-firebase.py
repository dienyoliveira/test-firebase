import requests
import unittest
from faker import Faker
import json
from jsonschema import validate


class TestFirebase(unittest.TestCase):
    schema = {"type": "object", "properties": {"Nome": {"type": "number"}}}

    def test_get_firebase(self):
        r = requests.get('https://test-json-9d3af.firebaseio.com/Agenda.json')
        print(r.content)
        response = json.loads(r.content)
        validate(response, schema=self.schema)

    def test_post_firebase(self):
        fake = Faker()

        for i in range(2):
            name = fake.name()
            print(name)
            data = '{"Nome": "'+name+'"}'
            print(data + '\n')
            r = requests.post('https://test-json-9d3af.firebaseio.com/Agenda.json', data=data)
            print(r.encoding)
            unittest.TestCase.assertEqual(self, r.encoding, 'utf-8', "The encoding is wrong!")
            print(r.elapsed)

            print(r.status_code)
            unittest.TestCase.assertEqual(self, r.status_code, 200, 'The conection is fail!')


if __name__ == "__main__":
    unittest.main()
