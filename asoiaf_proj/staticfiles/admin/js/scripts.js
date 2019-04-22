
fetch('{% url "overview_bar_chart_json" %}')
    .then(function (response) {
        return response.json();
    })
    .then(function (myJson) {
        console.log(JSON.stringify(myJson));
        const ctx = document.getElementById("gender").getContext("2d")
        new Chart(ctx, {
            type: 'bar',
            data: myJson
        });
    });

fetch('{% url "chapter_line_chart_json" %}')
    .then(function (response) {
        return response.json();
    })
    .then(function (myJson) {
        console.log(JSON.stringify(myJson));
        const ctx = document.getElementById("series").getContext("2d")
        new Chart(ctx, {
            type: 'line', data: myJson
        });
    });

// fetch('{% url "social_class_line_chart_json" %}')
//     .then(function (response) {
//         return response.json();
//     })
//     .then(function (myJson) {
//         console.log(JSON.stringify(myJson));
//         const ctx = document.getElementById("socialclass").getContext("2d")
//         new Chart(ctx, {
//             type: 'bar', data: myJson, options: {
//                 scales: {
//                     xAxes: [{
//                         display: true
//                     }],
//                     yAxes: [{
//                         ticks: {
//                             beginAtZero: true
//                         }
//                     }]
//                 }
//             }
//         });
//     })

// // fetch('{% url "manner_of_death_line_chart_json" %}')
// //     .then(function (response) {
// //         return response.json();
// //     })
// //     .then(function (myJson) {
// //         console.log(JSON.stringify(myJson));
// //         const ctx = document.getElementById("mannerofdeath").getContext("2d")
// //         new Chart(ctx, {
// //             type: 'bar', data: myJson, options: {
// //                 scales: {
// //                     xAxes: [{
// //                         display: true
// //                     }],
// //                     yAxes: [{
// //                         ticks: {
// //                             beginAtZero: true
// //                         }
// //                     }]
// //                 }
// //             }
// //         });
// //     });


// // fetch('{% url "death_by_book_json" %}')
// //     .then(function (response) {
// //         return response.json();
// //     })
// //     .then(function (myJson) {
// //         console.log(JSON.stringify(myJson));
// //         const ctx = document.getElementById("bookdeath").getContext("2d")
// //         new Chart(ctx, {
// //             type: 'line', data: myJson
// //         });
// //     });


