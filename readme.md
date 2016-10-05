## Quickstart

1. run `gcloud init`
2. open terminal to project directory and run `npm start`
3. open another terminal to same dir and run `gulp watch`
4. in package.json's deploy command, edit `{projectname}`
5. don't forget to `npm i`
6. go to localhost:8080/ to see your app
7. go to localhost:8000/ to see ndb interface


_note: updating files in template/ will not auto reload,  only files being watched by `gulp watch` will_

### __If building SPA__
- delete templates
- create index.html in src/



### __change:__
- main.py
in BaseHandler, the session name

- base.html
header info (title, etc)

- package.json
project name, git repo, etc

---


#### __Killing proc on port:__

sudo fuser -n tcp <port>
sudo kill -9 <id>

---

### __ACL__
https://cloud.google.com/storage/docs/access-control/create-manage-lists#defaultobjects
https://cloud.google.com/storage/docs/gsutil/commands/defacl  
__`gsutil defacl ch -u AllUsers:R gs://example-bucket`__  
will change future uploads to be publicly visible

---

### __Libraries__
Libraries supported by GAE must be listed in app.yaml  
Other libraries must be installed to 'lib' folder with  
`pip2.7 install --target=lib passlib`