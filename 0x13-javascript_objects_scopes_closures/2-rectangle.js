#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w) {
      this.width = w;
      this.height = h;
    } else {
      return undefined;
      }
    }
}
module.exports = Rectangle;
