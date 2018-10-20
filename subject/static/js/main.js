const getTopicListUrl = "/subject/getTopicsList/";

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

function getSubjectCode() {
  return parseUrl()[4];
}

function getTopicCode() {
  return parseUrl()[5];
}

function getTopicsList(subjectCode) {
  return JSON.parse(ajaxGet(getTopicListUrl + subjectCode)["topicList"]);
}

function displayTopicList() {
  var subjectCode = getSubjectCode();
  var topicList = getTopicsList(subjectCode);
  var out = "";
  topicList.forEach(topic => {
    out += `<li><a href="/subject/solve-topic/${subjectCode}/${topic.fields.function_code}/" class="btn btn-outline-primary">${topic.fields.title}</a></li>`;
  });
  $(".topic-list").html(out);
}

function getTopicExpressionUrl(subjectCode, topicCode) {
  return "/" + subjectCode + "/generate-expression/" + topicCode;
}

function refreshExercise() {
  var subjectCode = getSubjectCode();
  var topicCode = getTopicCode();

  var response = ajaxGet(getTopicExpressionUrl(subjectCode, topicCode));
  $("#expression-to-solve").html(response.expression);
}


function sendExpressionAnswer() {
  var expression = $("#expression-to-solve").html();
  var subjectCode = getSubjectCode();
  var topicCode = getTopicCode();
  var userAnswer = $("#answer").val();
  var data = {
    expression : expression,
    subjectCode: subjectCode,
    topicCode : topicCode,
    userAnswer : userAnswer
  };
  var response = postAjax("/" + subjectCode + "/solve-expression",data);
  showAnswer(response['isTrueAnswer']);
}

function showAnswer(resultAnswer) {
  $("#result").removeAttr("hidden");
  var printText = resultAnswer ? "True" : "False";
  $("#response").text(printText);
}

function hideAnswer() {
  $("#result").attr("hidden",'');
  $("#response").text('');
}

function requestNewExcecise() {
  hideAnswer();
  refreshExercise();
}