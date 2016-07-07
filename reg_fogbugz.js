#!/usr/bin/env node

var string = "BugzID: 123456";
var regex = /^BugzID: ([0-9]+)$/
var result = string.match(regex);
console.log('Hello, world!'+' result:'+result+'  '+result[1]+'  '+result[2]);