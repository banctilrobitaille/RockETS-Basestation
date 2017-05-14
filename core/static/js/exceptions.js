/**
 * Created by Benoit on 2017-05-03.
 */
function InvalidParameterException(message) {
    this.name = "InvalidParameterException";
    this.message = (message || "")
}

InvalidParameterException.prototype = Error.prototype;
