const express = require('express')
const router = express.Router()
const database = require('../database/database')

router.get('/', function (req, res, next) {
  res.render('addComplaint')
})

router.post('/', async function (req, res, next) {
  const rating = parseInt(req.body.rating)
  const complaint = req.body.complaint

  database.query(`INSERT INTO Complaints VALUES (${rating}, '${complaint}')`, function (error) {
    if (error) throw error
    console.log('Added to the table.')
  })
})

module.exports = router
