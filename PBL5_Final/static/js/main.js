var data_input = document.getElementById("data-input");
var time = parseInt(data_input.getAttribute("data-myinteger")); // 2 đoạn code dùng để lấy dữ liệu thời gian theo giây

var id_input = document.getElementById("id-input");
var id = parseInt(id_input.getAttribute("id-myinteger"));  // 2 đoạn code dùng để lấy id

var itemcountdown = document.querySelector('.coutdown-item'); // từ đây xún dùng để đếm ngược
function getCookie(name) {    // hàm lấy cookie
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

setInterval(function(){

  if (time == 0) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/student/end-time/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    var csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (csrfTokenInput) {
      var csrfToken = csrfTokenInput.value;
      xhr.setRequestHeader("X-CSRFToken", csrfToken); // Gửi CSRF token trong tiêu đề yêu cầu
    } else {
      console.error("Không tìm thấy đối tượng csrfTokenInput");
    }
    //clearInterval(countdownInterval); // Dừng đếm ngược khi time = 0
    var myid = id;
    var formData = {
      my_id: myid,
    };
  
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        var redirectUrl = response.redirect_url;
        window.location.href = redirectUrl;
      }
    };


    xhr.send(JSON.stringify(formData));
  }
  let giay = time % 60;
  let phut = Math.floor(time / 60);
  console.log(time);
  itemcountdown.innerHTML = `${phut} : ${giay}`;
  time--;
},1000)
// ham nay xu ly dem ngc thoi gian

