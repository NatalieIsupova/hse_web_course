// var a = 1;
// var a = "Hello world";

// for(var i=0;i<10;i++) {
// 	console.log(i);
// }
// var i = 0;
// while(i < 10){
// 	console.log(i) // вывод
// 	i++;

// 	if(i % 2 == 0) {
// 		continue; // перебрасывает в начало цикла
// 	}
// 	console.log("wow");

// 	if(i > 4) {
// 		break;
// 	}
// }
// // console.log(a);
// var i = 0.1;
// console.log(new Date());
// console.log([1,2,3]);
// var x = {"a": 15};
// console.log(x["a"]);

// function hello() {
// 	return 42
// }

// var hello = function () { // как лямбда функции, 
// 	return 42
// }

// var x = {"a": 15, "b": function() {
// 				return 43;
// 			}};
// console.log(x.b())
// console.log(x.a, x["b"])

// //iterate over properties
// var x = {"a": 15, "b": 20};
// for (var prop in x) {
// 	if (Object.prototype.hasOwnProperty.call(x, prop)) {
// 		console.log(prop, x[prop]);
// 	}
// }

// for(var a in [1,2,3]) {
// 	console.log(a);
// }


// function a() {
// 	var x;
// 	function b() {
// 		x = 1;
// 	}
// 	b();
// 	console.log(x);
// }
// a();

var a = '{"a": {"b": [1,2]}}';
console.log(a)


var a = '{"a": {"b": [1,2]}}',
	a_parsed = JSON.parse(a);
console.log(a_parsed.a.b)

