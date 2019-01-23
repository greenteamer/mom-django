import gql from 'graphql-tag'


export const me = gql`
  { 
    me {
      username
      tests {
        id
        inProgress
        totalPoints
        test {
          id
        }
        studentTestAnswers {
          id
          question {
            id
          }
          variant {
            id
          }
        }
      }
    }
    allTests {
      id
      name
      text
      testQuestions {
        id
        name
        text
        testQuestionVariants {
          id
          name
          value
          isCorrect
        }
      }
    }
  }
`
