import React from 'react'
import { map, forEach } from 'lodash'
import fp from 'lodash/fp'
import { withApollo, graphql } from 'react-apollo'
import { styled, Button } from 'reakit'
import { createStudentTestAnswer } from '../graphql/mutations'
import { observable, decorate, computed, action } from 'mobx'
import { observer } from 'mobx-react'

import Question from './Question'


@observer
class TestScreen extends React.Component { 
  pickedVariants = []

  state = {
    currentVariants: [],
    currentQuestion: null,
  }

  updatePickedVariants = ({ question, variant }) => {
    const findById = v => v.vId === variant.id
    const item = fp.find(findById)(this.pickedVariants)
    if (item) {
      this.pickedVariants.remove(item)
    } else {
      this.pickedVariants.push({
        vId: variant.id,
        qId: question.id,
      })
    }
  }

  get flatPickedVariants() {
    return fp.map(v => v.vId)(this.pickedVariants)
  }

  handleOnPickVariant = question => variant => {
    this.updatePickedVariants({ question, variant })
  }

  handleOnSave = () => {
    const { mutate, studentTest } = this.props
    forEach(this.pickedVariants, v => {
      const input = {
        testId: parseInt(studentTest.id, 10),
        variantId: parseInt(v.vId, 10),
        questionId: parseInt(v.qId, 10),
      }
      mutate({
        variables: {
          input,
        },
      })
    })
  }

  render() { 
    const { test, onClose } = this.props
    return (
      <Container>
        <Content>
          <h4>{test.name}</h4>
          {test && map(test.testQuestions, (question, index) => (
            <Question
              key={index}
              question={question}
              onPickHandler={this.handleOnPickVariant(question)}
              selectedVariants={this.flatPickedVariants}
            />
          ))}
        </Content>
        <ButtonWrapper>
          <MyButton red={true} onClick={onClose}>Закрыть</MyButton>
          <MyButton
            onClick={() => {
              this.handleOnSave()
              onClose()
            }}
          >Завершить тест</MyButton>
        </ButtonWrapper>
      </Container>
    )
  }
}

decorate(TestScreen, {
  pickedVariants: observable,
  updatePickedVariants: action,
  flatPickedVariants: computed,
})

export default withApollo(graphql(createStudentTestAnswer)(TestScreen))

const Container = styled.div`
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: white;
  z-index: 999;
  overflow-y: scroll;
`
const Content = styled.div`
  padding: 16px;
`
const ButtonWrapper = styled.div`
  position: fixed;
  bottom: 0;
  height: 60px;
  width: 100%;
  background: white;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0px 2px 92px 0px rgba(0, 0, 0, 0.2);
`
const MyButton = styled(Button)`
  margin: 8px;
  background-color: ${props => props.red && 'red' || '#2196f3'}
`
