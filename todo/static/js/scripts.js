let theme = document.querySelector("#theme");
let body = document.querySelector("body");
let tbody = document.querySelector("table");
let links = document.querySelectorAll("a");

let color = localStorage.getItem("color");
if (color === null) {localStorage.setItem("color", "light")}

body.style.fontFamily = "monospace";

function altera_tema () {
	color = localStorage.getItem("color");
	if (color === "light") {
		body.style.backgroundColor = "#484848";
		body.style.color = "#cccccc";
		tbody.style.color = "#cccccc";
		for (let i = 0; i < links.length; i++) {
			links[i].style.color = "#cccccc";
		}
		body.style.transition = ".2s";
	} else {
		body.style.backgroundColor = "#ffffff";
		body.style.color = "#000000";
		tbody.style.color = "#000000";
		for (let i = 0; i < links.length; i++) {
			links[i].style.color = "#000000";
		}
		body.style.transition = ".2s";
	}
}

theme.onclick =	function () {
	color = localStorage.getItem("color");
	console.log("clique");
	if (color === "light") {
		localStorage.setItem("color", "dark");
		theme.innerHTML = "Dark";
	} else if (color === "dark") {
		localStorage.setItem("color", "light");
		theme.innerHTML = "Light";
	}
	altera_tema();
}

altera_tema();


let btnRemove = document.querySelectorAll(".btn-remove");

for (let i = 0; i < btnRemove.length; i++){
	btnRemove[i].onclick = function (e) {
		e.preventDefault();
		path = btnRemove[i].getAttribute('href');
		conf = confirm("Tem certeza que deseja excluir esta tarefa?")
		if (conf === true) {
			location.href = path;
		}
	}
}