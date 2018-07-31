import json
import os
import base64
import time

from images_classifiers.cf.classifiers import CaffeNsfwResnetClassifier

classifier = CaffeNsfwResnetClassifier(mode_gpu=False)

batch_size = 1

for filename in os.listdir('test_files/'):
    path = os.path.join('test_files/', filename)

    with open('indexed_test_files/nsfw_{}'.format(filename), mode='a') as output_file:
        with open(path) as input_file:
            print('******* {}'.format(path))

            for line in input_file:
                batch_json_docs = []
                batch_img = []

                start = time.time()
                try:
                    json_doc = json.loads(line)
                except Exception as e:
                    print(e)
                    print(line)

                batch_json_docs.append(json_doc)
                batch_img.append(base64.b64decode(json_doc['imgSrcBase64']))

                if len(batch_img) == batch_size:
                    results = classifier.classify_batch(batch_img)
                    for i in range(len(results)):
                        json_doc = batch_json_docs[i]
                        json_doc['safe'] = results[i]
                        output_file.write(json.dumps(json_doc))
                    end = time.time()
                    print('Records / Second: {}'.format(batch_size/(end - start)))

            if len(batch_img) != 0:
                results = classifier.classify_batch(batch_img)
                for i in range(len(results)):
                    json_doc = batch_json_docs[i]
                    json_doc['safe'] = results[i]
                    output_file.write(json.dumps(json_doc))