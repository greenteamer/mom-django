document.addEventListener('DOMContentLoaded', function() {

  Vue.component('question-item', {
    props: ['question'],
    template: `
      <li>{{ question.name }}</li>
    `,
  })

  new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
      title: 'Welcome to My Journal',
      test: {
        name: "my test name",
        questions: [
          {
            id: 1,
            name: 'my question name',
            text: 'my question text',
          },
          {
            id: 2,
            name: 'my question name1',
            text: 'my question text1',
          },
          {
            id: 3,
            name: 'my question name1',
            text: 'my question text1',
          },
        ],
      },
      questions: [1, 2, 3],
      message: 'Вы загрузили эту страницу: ' + new Date().toLocaleString(),
    },
    methods: {
      handleOnClick: function () {
        this.test.questions.push({ name: 'new name', text: 'new text ' });
      }
    }
  });
});