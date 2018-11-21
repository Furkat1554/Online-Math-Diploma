function getIsUserEnrolledUrl(streamCode) {
  return `/subject/stream/${streamCode}/is-enrolled`;
}

function getEnrollUserUrl() {
  return `/subject/stream/enroll_user/`;
}

function getAssignmentsUrl() {

}

function loadStreamDetailsPage() {

}

function isUserEnrolled(data = {}) {
  var userId = null;
  var streamCode = null;
  if (data.hasOwnProperty('userId')) {
    userId = data['userId'];
  }
  if (data.hasOwnProperty('streamCode')) {
    streamCode = data['streamCode'];
  }
  if (isEmptyVar(streamCode)) {
    streamCode = getPrimaryCode();
  }
  if (isEmptyVar(streamCode)) {
    return responseError({
      errorMessage: "No stream code is provided"
    });
  }
  var result = postAjax(getIsUserEnrolledUrl(streamCode));
  return result;
}

function displayEnrollAccess(isEnrolled) {
  if (isEnrolled) {
    $('#enrolled-section').removeAttr('hidden');
  }
  if (!isEnrolled) {
    $('#not-enrolled-section').removeAttr('hidden');
  }
}

function enrollRequest(data) {
  if (data == null) {
    return {
      'errorMessage': 'Invalid data'
    }
  }
  if (!data.hasOwnProperty('streamCode')) {
    data['streamCode'] = getPrimaryCode();
  }
  return postAjax(getEnrollUserUrl(), data);

}

function enrollUser(enrollKey, userId = 0) {
  var data = {
    userId: userId,
    enrollKey: enrollKey,
    enrollOperation: true
  };
  return enrollRequest(data);
}

function unEnrollUser(userId = 0) {
  var data = {
    userId: userId,
    enrollOperation: false
  };
  return enrollRequest(data);
}

function getAssignments(data = {}) {
  if(!data.hasOwnProperty('userId'))
    data['userId'] = 0;
  var response = postAjax(`/subject/assignments/`, data);
  return response['assignments'];
}

function getStreamAssignmentsDetails(streamCode, userId = 0) {
  if (isEmptyVar(streamCode)) {
    streamCode = getPrimaryCode();
  }
  var data = {
    userId: userId,
    streamCode: streamCode
  };
  var assignment = getAssignments(data);
  return assignment;
}

function dislpayStreamAssignmentDetails(assignments) {
  if (null == assignments) {
    assignments = getStreamAssignmentsDetails();
  }
  var out = `<ul id="assignment-list">`;
  assignments.assigmnents.forEach((assignment) => {
    out += `<li id=""></li>`;
  });
  out += ``;
  out += `</ul>`
}