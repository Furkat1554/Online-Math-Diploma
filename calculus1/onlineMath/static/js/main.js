const getTopicListUrl = "/subject/getTopicsList/";
const getStreamListUrl = "/subject/streams";

function ajaxGet(reqUrl) {
  var s = {};
  $.ajax({
    async: false,
    url: reqUrl,
    type: "GET",
    dataType: "json",
    success: function (data) {
      s = data;
    }
  });
  return s;
}

function postAjax(reqUrl, sendData) {
  let response;
  $.ajax({
    async: false,
    type: "POST",
    url: reqUrl,
    dataType: "json",
    data: sendData,
    success: function (p) {
      response = p;
    },
    error: function (err) {
      response = err;
    },
  });
  return response;
}

function parseUrl() {
  return (window.location.href).split("/")
    .filter(str => null != str && str.trim() !== "");
}

function getPrimaryCode() {
  return parseUrl()[4];
}

function getSecondaryCode() {
  return parseUrl()[5];
}

function getTopicsList(subjectCode) {
  return JSON.parse(ajaxGet(getTopicListUrl + subjectCode)["topicList"]);
}

function getStreamList() {
  return JSON.parse(ajaxGet(getStreamListUrl).streamList);
}

function getTopicExpressionUrl(subjectCode, topicCode) {
  return "/" + subjectCode + "/generate-expression/" + topicCode;
}

function getStreamDetails(streamCode) {
  if (isEmptyVar(streamCode)) {
    streamCode = getPrimaryCode();
  }
  if (isEmptyVar(streamCode)) {
    console.log("empty");
    return {}
  }
  var details = ajaxGet(`/subject/stream/${ streamCode }/details`);
  details.stream = JSON.parse(details.stream);
  return details;
}

function displayTopicList() {
  var subjectCode = getPrimaryCode();
  var topicList = getTopicsList(subjectCode);
  var out = "";
  topicList.forEach(topic => {
    out += `<li><a 
                href="/subject/solve-topic/${subjectCode}/${topic.fields.function_code}/" 
                class="btn btn-outline-primary mb-1">${topic.fields.title}</a></li>`;
  });
  $(".topic-list").html(out);
}

function displayStreamList() {
  var streamList = getStreamList();
  console.log(streamList);
  var out = "";
  streamList.forEach(stream => {
    out += `<li><a href="/subject/streams/${ stream.fields.stream_code }/" class="btn btn-primary mb-1">${ stream.fields.title }</a></li>`;
  });
  $("#stream-list").html(out);
}

function refreshExercise() {
  var subjectCode = getPrimaryCode();
  var topicCode = getSecondaryCode();

  var response = ajaxGet(getTopicExpressionUrl(subjectCode, topicCode));
  console.log(response);
  $("#expression-to-solve").html(response.expression);
}

function sendExpressionAnswer() {
  var expression = $("#expression-to-solve").html();
  var subjectCode = getPrimaryCode();
  var topicCode = getSecondaryCode();
  var userAnswer = $("#answer").val();
  var data = {
    expression: expression,
    subjectCode: subjectCode,
    topicCode: topicCode,
    userAnswer: userAnswer
  };
  var response = postAjax("/" + subjectCode + "/solve-expression", data);
  showAnswer(response['isTrueAnswer']);
}

function showAnswer(resultAnswer) {
  $("#result").removeAttr("hidden");
  var printText = resultAnswer ? "True" : "False";
  $("#response").text(printText);
}

function hideAnswer() {
  $("#result").attr("hidden", '');
  $("#response").text('');
}

function requestNewExercise() {
  hideAnswer();
  refreshExercise();
}

function isEmptyVar(variable) {
  return variable == null || variable == '';
}

function responseError(data) {
  var errorCode = data['errorCode'];
  var errorMessage = data['errorMessage'];
  var properties = data['properties'];
  return {
    errorCode: errorCode,
    message: errorMessage,
    properties: properties
  }
}