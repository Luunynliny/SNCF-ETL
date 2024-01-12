/////////////////////////
// Rerieve credentials //
/////////////////////////

load("/docker-entrypoint-initdb.d/CREDENTIALS.js")

///////////////////////
// Create a new user //
///////////////////////

db.createUser({
    user: credentials.username,
    pwd: credentials.password,
    roles: [
        {
            role: 'readWrite',
            db: 'sncf'
        }
    ]
})

/////////////////////////
// Create new database //
/////////////////////////

db = new Mongo().getDB('sncf')

///////////////////////////
// Create new collection //
///////////////////////////

db.createCollection('train_stops')