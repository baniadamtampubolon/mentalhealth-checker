function generateRandom() {
  for (let i = 1; i <= 27; i++) {
    const select = document.getElementsByName(`feature${i}`)[0];
    const randomValue = Math.random() < 0.5 ? "0" : "1";
    select.value = randomValue;
  }
  alert("Field Yes/No berhasil diisi dengan nilai acak untuk testing!");
}
