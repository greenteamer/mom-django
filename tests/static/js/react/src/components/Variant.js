import React from 'react'
import { styled } from 'reakit'


class Variant extends React.Component { 
  render() { 
    const { variant, onPickHandler, isSelected } = this.props
    return (
      <VariantContainer onClick={() => onPickHandler(variant)} isSelected={isSelected}>
        <Name isSelected={isSelected}>{variant.name}</Name>
      </VariantContainer>
    )
  }
}

export default Variant

const VariantContainer = styled.div`
  padding: 8px;
  margin: 8px 0;
  border: 1px solid #3477bb;
  border-radius: 4px;
  background-color: ${props => props.isSelected ? '#3477bb' : 'white'};
  &:hover {
    cursor: pointer;
  }
`

const Name = styled.p`
  font-size: 16px;
  color: ${props => props.isSelected ? 'white' : 'black'};
`