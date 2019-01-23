import React from 'react'
import { styled } from 'reakit'
import { map } from 'lodash'
import Variant from './Variant'


class Question extends React.Component { 

  isSelected = variantId => {
    const { selectedVariants } = this.props
    const isSelected = selectedVariants.includes(variantId)
    console.log('>>> Question isSelected() isSelected: ', isSelected)
    return isSelected
  }

  render() {
    const { question, onPickHandler } = this.props
    return (
      <QuestionContainer>
        <QuestionName>{question.name}</QuestionName>
        <QuestionName>{question.text}</QuestionName>
        {map(question.testQuestionVariants, (variant, index) => (
          <Variant
            key={index}
            variant={variant}
            onPickHandler={onPickHandler}
            isSelected={this.isSelected(variant.id)}
          />
        ))}
      </QuestionContainer>
    )
  }
}

export default Question

const QuestionContainer = styled.div`
  margin: 64px 0;
`

const QuestionName = styled.p`
  font-size: 16px;
`