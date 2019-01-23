import gql from 'graphql-tag'


export const createStudentTest = gql`
  mutation CreateStudentTest($input: StudentTestCreateInput!) {
    createStudentTest(input: $input) {
      studentTest {
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
  }
`

export const createStudentTestAnswer = gql`
  mutation CreateStudentTestAnswer($input: StudentTestAnswerCreateInput!) {
    createStudentTestAnswer(input: $input) {
      studentTest {
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
  }
`