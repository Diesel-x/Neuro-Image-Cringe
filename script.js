document.getElementById("fileInput").onchange = function (event) {
  var reader = new FileReader();
  reader.onload = function (e) {
    var uploadedImage = document.getElementById("uploadedImage");
    uploadedImage.src = e.target.result;
    uploadedImage.style.display = "block";
  };
  reader.readAsDataURL(document.getElementById("fileInput").files[0]);
  document.getElementById("predictionResult").textContent = "";
};

document.getElementById("fileInput").addEventListener("change", predict);
document.getElementById("fileBtn").addEventListener("click", pick);

function pick() {
  document.getElementById("fileInput").click();
}

function predict() {
  var fileInput = document.getElementById("fileInput");
  var file = fileInput.files[0];
  if (!file) {
    alert("Please select a file.");
    return;
  }

  resultText = "sfsdfds";
  var formData = new FormData();
  formData.append("image", file);
  fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      switch (data.Class) {
        case "Non Sonic & Shadow":
          resultText = `На изображении нет Соника и Шедоу с вероятностью ${Math.round(
            data.Score * 100
          )}%`;
          break;
        case "Sonic":
          resultText = `На изображении Соник с вероятностью ${Math.round(
            data.Score * 100
          )}%`;
          break;
        case "Shadow":
          resultText = `На изображении Шедоу с вероятностью ${Math.round(
            data.Score * 100
          )}%`;
          break;
      }
      var predictionResult = document.getElementById("predictionResult");
      predictionResult.textContent = resultText;
      //   predictionResult.textContent = `Изображение содержит ${
      //     data.Class
      //   } на ${Math.round(data.Score * 100)}%`;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
