Attribute VB_Name = "Module1"
Sub DownloadDataset()

    Dim URL             As String
    Dim objXmlHttpReq   As Object
    
    URL = "https://community.tableau.com/sfc/servlet.shepherd/document/download/0694T000001GnpUQAS?operationContext=S1"
    Set objXmlHttpReq = CreateObject("MSXML2.XMLHTTP")
    
    objXmlHttpReq.Open "GET", URL, False
    objXmlHttpReq.send
    
    If objXmlHttpReq.Status = 200 Then
        Set objStream = CreateObject("ADODB.Stream")
        objStream.Open
        objStream.Type = 1
        objStream.Write objXmlHttpReq.responseBody
        objStream.SaveToFile ThisWorkbook.Path & "\" & "SourceData.xls", 2
        objStream.Close
    End If

End Sub

Sub ImportSheets()

Dim sourceFile          As String
Dim sheet               As Worksheet
Dim WS_Count            As Integer

sourceFile = ThisWorkbook.Path & "\" & "SourceData.xls"

Set twb = ThisWorkbook
Set wb = Workbooks.Open(sourceFile)

For Each sheet In wb.Sheets
    Debug.Print (sheet.Name)
    wb.Worksheets(sheet.Name).Copy _
    after:=twb.Worksheets(1)
Next sheet

wb.Close

End Sub

Sub DeleteFile()

sourceFile = ThisWorkbook.Path & "\" & "SourceData.xls"
Kill sourceFile

End Sub

Sub PeopleCleanup()

Set ws = ThisWorkbook.Worksheets("People")

    ws.Range("A2:B5").ClearContents

    Sheets("Orders").Range("G2", Sheets("Orders").Range("G2").End(xlDown)).Copy Sheets("People").Range("A2")
    Sheets("People").Range("A2", Sheets("People").Range("A2").End(xlDown)).RemoveDuplicates Columns:=1, Header:=xlNo

    ws.Range("C1").FormulaR1C1 = "CustomerID"
    ws.Range("D1").FormulaR1C1 = "Segment"
    ws.Range("E1").FormulaR1C1 = "Order Count"
    ws.Range("F1").FormulaR1C1 = "Avg_Profit"
    ws.Range("G1").FormulaR1C1 = "ReturnCount"
    
    ws.Range("C2").FormulaR1C1 = "=INDEX(Orders!C[3], MATCH(RC[-2], Orders!C[4], FALSE))"
    ws.Range("D2").FormulaR1C1 = "=VLOOKUP(RC[-3], Orders!C[3]:C[4], 2, FALSE)"
    ws.Range("E2").FormulaR1C1 = "=COUNTIF(Orders!C[2], RC[-4])"
    ws.Range("F2").FormulaR1C1 = "=AVERAGEIF(Orders!C[1], People!RC[-5], Orders!C[15])"
    ws.Range("G2").FormulaR1C1 = "=SUMIF(Orders!C[-1], People!RC[-4], Orders!C[15])"
    
    ws.Range("C2:G2").AutoFill Destination:=Range("C2:G794")

End Sub

Sub OrdersCleanup()

Set ws = ThisWorkbook.Worksheets("Orders")

    ws.Range("V1").FormulaR1C1 = "Returns"
    ws.Range("V2").FormulaR1C1 = "=IF(ISNA(MATCH(RC[-20], Returns!C[-20], FALSE)), 0, 1)"
    ws.Range("V2").AutoFill ws.Range("V2:V" & ws.Range("A" & Rows.Count).End(xlUp).Row)

End Sub






