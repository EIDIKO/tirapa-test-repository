import xlsxwriter

# Sample data
data = [
    {
        'ISSUE_URL': 'URL1',
        'ISSUE_NUMBER': 1,
        'ISSUE_TITLE': 'Title1',
        'COMMENT_URL': 'Comment URL1',
        'ASS_LOGIN': 'Assignee1',
        'ASS_TYPE': 'Type1',
    },
    {
        'ISSUE_URL': 'URL2',
        'ISSUE_NUMBER': 2,
        'ISSUE_TITLE': 'Title2',
        'COMMENT_URL': 'Comment URL2',
        'ASS_LOGIN': 'Assignee2',
        'ASS_TYPE': 'Type2',
    },
]

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

# Write headers
headers = ['ISSUE_URL', 'ISSUE_NUMBER', 'ISSUE_TITLE', 'COMMENT_URL', 'ASS_LOGIN', 'ASS_TYPE']
for col, header in enumerate(headers):
    worksheet.write(0, col, header)

# Write data
for row, item in enumerate(data):
    for col, key in enumerate(headers):
        worksheet.write(row + 1, col, item.get(key, ''))

workbook.close()
