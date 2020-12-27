---
layout: post
title:  "mongodb创建索引(index)"
date: 2020-02-12 09:18:04
categories: [数据库, mongodb]
tags: [mongodb, goland]
excerpt_separator: <!--more-->
---
mongodb创建索引(index)
<!--more-->

mongodb官方go driver

```go

// createIndexes 创建索引
func createIndexes(client *mongo.Client) error {
	cReading := client.Database(databaseCoredata).Collection(collectionReading)
	indexes := map[string]mongo.IndexModel{
		"_device_created_name_": {
			Keys:    bsonx.Doc{
				{"device", bsonx.Int32(1)},
				{"created", bsonx.Int32(1)},
				{"name", bsonx.Int32(1)},
			},
			Options: options.Index().SetBackground(true).SetName("_device_created_name_"),
		},
		"_device_": {
			Keys:    bsonx.Doc{
				{"device", bsonx.Int32(1)},
			},
			Options: options.Index().SetBackground(true).SetName("_device_"),
		},
		"_created_": {
			Keys:    bsonx.Doc{
				{"created", bsonx.Int32(1)},
			},
			Options: options.Index().SetBackground(true).SetName("_created_"),
		},
		"_name_": {
			Keys:    bsonx.Doc{
				{"name", bsonx.Int32(1)},
			},
			Options: options.Index().SetBackground(true).SetName("_name_"),
		},
	}

	cursor, err := cReading.Indexes().List(context.Background())
	if err != nil {
		logrus.Fatalln(err)
	}
	for cursor.Next(context.Background()) {
		var idx index
		err := cursor.Decode(&idx)
		if err != nil {
			logrus.Warningln("Decode Index error", err)
			continue
		}
		delete(indexes, idx.Name)
	}
	models := []mongo.IndexModel{}
	for _, v := range indexes {
		models = append(models, v)
	}
	if len(models) > 0 {
		names, err := cReading.Indexes().CreateMany(context.Background(), models)
		if err != nil {
			logrus.Fatalln(err)
		}
		logrus.Infoln("Create Indexes", names)
	}
	return err
}
```