import React from 'react'
import { styled } from 'reakit'
import { withApollo, graphql } from 'react-apollo'
import { get, find } from 'lodash'

import TestScreen from './TestScreen'
import { createStudentTest } from '../graphql/mutations'
import Button from './common/Button'
import { me as queryMe } from '../graphql/queries'


class TestInfo extends React.Component { 

  state = {
    studentTest: null,
    showTest: false,
  }

  toggleShowTest = () => {
    this.setState({
      showTest: !this.state.showTest,
    })
  }

  handlerOnStartTest = () => {
    const { test, mutate, me, client } = this.props
    if (!me) {
      return
    }
    const inProgressTests = find(me.tests, t => {
      return t.test.id === test.id && t.inProgress
    })
    if (inProgressTests) {
      this.setState({
        studentTest: inProgressTests,
      })
      this.toggleShowTest()
    } else {
      // ELSE create new inProgress test
      const input = {
        testId: test.id,
      }
      mutate({
        variables: {
          input,
        },
      }).then(result => {
        const studentTest = get(result, ['data', 'createStudentTest', 'studentTest'])

        const data = client.readQuery({ query: queryMe })
        client.writeQuery({
          query: queryMe,
          data: {
            ...data,
            me: {
              ...data.me,
              tests: [...data.me.tests, studentTest],
            }
          },
        })

        this.setState({
          studentTest,
        })
        this.toggleShowTest()
      }).catch(error => {
        console.log('>>>> mutate error: ', { error })
      })
    }

  }

  render() {
    const { test } = this.props
    const { showTest, studentTest } = this.state
    return (
      <Container>
        <Name>{test.name}</Name>
        <Text>{test.text}</Text>
        <Button onClick={this.handlerOnStartTest}>Пройти тест</Button>
        {showTest &&
          <TestScreen
            test={test}
            studentTest={studentTest}
            onClose={this.toggleShowTest}
          />
        }
      </Container>
    )
  }
}

export default withApollo(graphql(createStudentTest)(TestInfo))

const Container = styled.div`
  margin: 16px 0 32px;
`

const Name = styled.p`
  font-size: 22px;
  margin: 16px 0 8px;
`

const Text = styled.p`
  font-size: 14px;
`