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

  var isButtonClicked = false; // Biến cờ để kiểm soát việc gọi hàm
  var completeButton = document.getElementById("complete-button"); // Lấy tham chiếu đến nút hoàn tất
  completeButton.addEventListener("click", function(event) {
    isButtonClicked = true; // Đặt giá trị của biến cờ thành true khi nút hoàn tất được bấm
  });

window.addEventListener("beforeunload", function(event) {
    if (!isButtonClicked && time > 0) {     // nếu bấm hoàn tất và khi thời gian lớn hơn 0 hàm lấy thời gian thoát sẽ không chạy

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/student/save-exit-time/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
  
    var csrftoken = getCookie('csrftoken'); // Lấy CSRF token từ cookie
    xhr.setRequestHeader("X-CSRFToken", csrftoken); // Gửi CSRF token trong tiêu đề yêu cầu
    var csrfTokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
        if (csrfTokenInput) {
        var csrfToken = csrfTokenInput.value;
        // Tiếp tục xử lý với csrfToken
            } else {
          console.error("Không tìm thấy đối tượng csrfTokenInput");
        }
    console.log("");

    var exittime  = time;
    var myid = id;
    var data = {
      exit_time: exittime,
      my_id: myid,
    };
  
    xhr.send(JSON.stringify(data));

  }
  });