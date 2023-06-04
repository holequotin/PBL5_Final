var data_input = document.getElementById("data-input");
var time = parseInt(data_input.getAttribute("data-myinteger")); // 2 đoạn code dùng để lấy dữ liệu thời gian theo giây

var id_input = document.getElementById("id-input");
var id = parseInt(id_input.getAttribute("id-myinteger"));  // 2 đoạn code dùng để lấy id

var itemcountdown = document.querySelector('.coutdown-item'); // từ đây xún dùng để đếm ngược
setInterval(function(){
  let giay = time % 60;
  let phut = Math.floor(time / 60);

  itemcountdown.innerHTML = `${phut} : ${giay}`;
  time--;
},1000)
// ham nay xu ly dem ngc thoi gian

