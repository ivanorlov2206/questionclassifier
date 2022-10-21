from Writers.BasicWriter import BasicWriter


class HtmlWriter(BasicWriter):
    def write(self, predictionResult):
        group_rows = ""
        for group_i in range(len(predictionResult.predictionGroups)):
            group = predictionResult.predictionGroups[group_i]
            group_rows += "<tr>"
            group_rows += "<td>"
            for sent_i in range(len(group.sentences)):
                sent = group.sentences[sent_i][1]
                group_rows += sent + "<br/>"
            group_rows += "</td>"
            group_rows += "</tr>"

        content = '''
            <html>
                <head>
                    <meta charset="utf-8">
                </head>
                <body>
                    <table border='1'>
                        {}
                    </table>
                </body>
            </html>
        '''.format(group_rows)
        f = open(self.path, "w", encoding="utf-8")
        print(content, file=f)
        f.close()