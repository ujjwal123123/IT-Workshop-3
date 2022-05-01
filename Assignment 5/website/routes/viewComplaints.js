const express = require('express')
const router = express.Router()
const database = require('../database/database')

router.get('/', async function (req, res, next) {
  database.query('SELECT * FROM Complaints', function (error, complaints) {
    if (error) throw error
    res.render('viewComplaints', { complaints: complaints })
  })
})

module.exports = router
