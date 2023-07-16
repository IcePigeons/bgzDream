import os.path

from docxtpl import DocxTemplate

from docHandle.models import MtaInfo, MtaConclusion


# import subprocess
# import os

# try:
#     from comtypes import client
# except ImportError:
#     client = None
# try:
#     from win32com.client import constants, gencache
# except ImportError:
#     constants = None
#     gencache = None


class FileUtil:
    # 民太安模板内容docx内容替换
    @staticmethod
    def replaceDocxContent(mtaInfo: MtaInfo, mtaCheckHospitalArr: list, mtaUnCheckHospitalArr: list,
                           mtaConclusion: MtaConclusion):
        # print(os.path.abspath("DocxTemplate/mta-template.docx"))
        doc = DocxTemplate(os.path.abspath("DocxTemplate/mta-template.docx"))  # 选定模板
        # 需要替换的内容
        context = {
            'name': mtaInfo.name,
            'card': mtaInfo.card,
            'sex': mtaInfo.sex,
            'address': mtaInfo.address,
            'phone': mtaInfo.phone,
            'callTime': mtaInfo.callTime,
            'policyNumber': mtaInfo.policyNumber,
            'reportNumber': mtaInfo.reportNumber,
            'principalDate': mtaInfo.principalDate,
            'kindInsurance': mtaInfo.kindInsurance,
            'dateInsurance': mtaInfo.dateInsurance,
            'caseDesc': mtaInfo.caseDesc,
            'workMedicare': mtaInfo.workMedicare,
            'bodyHealth': mtaInfo.bodyHealth,
            'outpatient': mtaInfo.outpatient,
            'hospital': mtaInfo.hospital,
            'outpatientNum': count(mtaInfo.outpatient),  # 门诊次数统计
            'hospitalNum': count(mtaInfo.hospital),  # 住院次数统计
            'lifeTrackInfo': mtaInfo.lifeTrackInfo,
            'location': mtaInfo.address[:9],  # 所在地
            # 排查医院信息数组
            'mtaCheckHospitalArr': mtaCheckHospitalArr,
            'mtaUnCheckHospitalArr': mtaUnCheckHospitalArr,
            'mtaConclusion': mtaConclusion
        }
        doc.render(context)  # 渲染替换
        fileName = mtaInfo.name + "-调查报告 民太安.docx"
        filePath = "DocxTemplate/out/"
        file = filePath + fileName
        if os.path.isfile(file):
            os.remove(file)
        doc.save(file)  # 保存
        return file
    @staticmethod
    def docx2pdf():
        pass

    @staticmethod
    def pdf2docx():
        pass


def count(s: str):
    return s.count("、")

#
# def doc2pdf_linux(docPath, pdfPath):
#     """
#     convert a doc/docx document to pdf format (linux only, requires libreoffice)
#     :param doc: path to document
#     """
#     cmd = 'libreoffice6.3 --headless --convert-to pdf'.split() + [docPath] + ['--outdir'] + [pdfPath]
#     p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#     p.wait(timeout=30)
#     stdout, stderr = p.communicate()
#     if stderr:
#         raise subprocess.SubprocessError(stderr)
# def doc2pdf(docPath, pdfPath):
#     """
#         convert a doc/docx document to pdf format
#         :param doc: path to document
#         """
#     docPathTrue = os.path.abspath(docPath)  # bugfix - searching files in windows/system32
#     if client is None:#判断环境，linux环境这里肯定为None
#         return doc2pdf_linux(docPathTrue, pdfPath)
#     word = gencache.EnsureDispatch('Word.Application')
#     doc = word.Documents.Open(docPathTrue, ReadOnly=1)
#     doc.ExportAsFixedFormat(pdfPath,
#                             constants.wdExportFormatPDF,
#                             Item=constants.wdExportDocumentWithMarkup,
#                             CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
#     word.Quit(constants.wdDoNotSaveChanges)
# if __name__ == '__main__':
#     wordpath='/var/db/Report_20191206105753.docx'
#     pdfpath='/var/db'
#     doc2pdf(wordpath,pdfpath)
