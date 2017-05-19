/**
 * Created by Benoit on 2017-05-03.
 */
function validateRemoteSensorParameters(sensorName, sensorNode) {
    validateSensorName(sensorName);
    validateSensorNode(sensorNode);
}

function validateLocalSensorParameters(sensorName) {
    validateSensorName(sensorName);
}

function validateSensorNode(sensorNode) {
    if (isNullOrEmpty(sensorNode)) {
        $("#sensorNodeError").show();
        throw new InvalidParameterException("A remote sensor should have an associated node");
    } else {
        $("#sensorNodeError").hide();
    }
}

function validateSensorName(sensorName) {
    if (isNullOrEmpty(sensorName)) {
        $("#sensorNameError").show();
        throw new InvalidParameterException("Sensor name should not be empty");
    } else {
        $("#sensorNameError").hide();
    }
}

function isNullOrEmpty(parameter) {
    return (!parameter || parameter === "");
}
