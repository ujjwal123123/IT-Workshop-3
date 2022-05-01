require('dotenv').config()

const mysql = require('mysql')

const connection = mysql.createConnection({
  host: process.env.RDS_HOSTNAME,
  user: process.env.RDS_USERNAME,
  password: process.env.RDS_PASSWORD
})

connection.connect(function (err) {
  if (err) throw err
  console.log('Connected!')
  connection.query(`CREATE DATABASE IF NOT EXISTS ${process.env.RDS_DB_NAME}`, function (err, result) {
    if (err) throw err
    console.log('Database created')
    connection.changeUser({ database: process.env.RDS_DB_NAME }, function (err) {
      if (err) throw err

      console.log(`Now connected to the database ${process.env.RDS_DB_NAME}`)
      connection.query('CREATE TABLE IF NOT EXISTS Complaints(rating int, complaint varchar(100))', function (err) {
        if (err) throw err
      })
    })
  })
})

module.exports = connection
