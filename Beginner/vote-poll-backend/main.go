package main

import (
	"gorm.io/gorm"
)


type Poll struct {
	id uint `json:"id" gorm:"primaryKey"`
	question string `json:"question"`
	Options []Option  `json:"options" gorm:"foreignKey:PollID"`

}

type Option struct {
	id uint `json:"id" gorm:"primaryKey"`
	text string `json:"text"`
	votes int `json:"votes"`
	PollID uint `json:"poll_id"`
}

var db *gorm.DB


