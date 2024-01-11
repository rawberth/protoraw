from io import BytesIO
from pathlib import Path

from weasyprint import HTML
from wand.image import Image
from wand.color import Color



output = (
    Path(__file__).parent
    / 'htmlimage.png')

html_string = """
    <style>

      * {
        border-collapse: collapse;
        border-spacing: 0px;
        border-width: 0px 0px 0px 0px;
        box-sizing: border-box;
        font-size: 6px;
        font-style: normal;
        line-height: 6px;
        list-style-type: none;
        padding: 0px 0px 0px 0px;
        page-break-after: avoid;
        page-break-before: avoid;
        page-break-inside: avoid;
        text-align: left;
        text-decoration: none;
        vertical-align: middle;
        white-space: nowrap;
        letter-spacing: 0.15px; }

      table.special thead td {
        background-color: #fdcf8d;
        padding: 2px 3px 2px 3px; }

      table.special tbody td {
        padding: 1px 2px 1px 2px; }

      table.special tbody
       tr:nth-child(even) td {
        background-color: #d7f6ff; }

      table.special tbody
       tr:nth-child(odd) td {
        background-color: #c7edfd; }

      td.vehicle_cost {
        text-align: right; }

      td.vehicle_discount {
        text-align: center; }

      table.special tbody
       tr:nth-child(even) td.vehicle_discount {
        background-color: #b9e1fb !important; }

      table.special tbody
       tr:nth-child(odd) td.vehicle_discount {
        background-color: #add2fc !important; }

    </style>
    <table>
     <tbody>
      <tr><td>
        <table class="special">
         <thead>
          <tr>
           <td colspan="3">Vehicle Sales</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td class="vehicle">Grotti GT500</td>
           <td class="vehicle_cost">$549,500</td>
           <td class="vehicle_discount">30%</td>
          </tr>
          <tr>
            <td class="vehicle">Gallivanter Baller LE</td>
            <td class="vehicle_cost">$374,000</td>
            <td class="vehicle_discount">-151%</td>
          </tr>
          <tr>
            <td class="vehicle">Grotti GT500</td>
            <td class="vehicle_cost">$549,500</td>
            <td class="vehicle_discount">30%</td>
          </tr>
          <tr>
            <td class="vehicle">Ubermacht SC1</td>
            <td class="vehicle_cost">$1,122,100</td>
            <td class="vehicle_discount">30%</td>
          </tr>
          <tr>
            <td class="vehicle">Benefactor Schafter LWB</td>
            <td class="vehicle_cost">$145,600</td>
            <td class="vehicle_discount">30%</td>
          </tr>
          <tr>
            <td class="vehicle">Dewbauchee Seven-70</td>
            <td class="vehicle_cost">$486,500</td>
            <td class="vehicle_discount">30%</td>
          </tr>
          <tr>
            <td class="vehicle">Benefactor XLS</td>
            <td class="vehicle_cost">$365,400</td>
            <td class="vehicle_discount">-44%</td>
          </tr>
          <tr>
            <td class="vehicle">Benefactor XLS (Armored)</td>
            <td class="vehicle_cost">$365,400</td>
            <td class="vehicle_discount">30%</td>
          </tr>
         </tbody>
        </table>
      </td></tr>
     </tbody>
    </table>
    """



tempfile = BytesIO()
html = HTML(string=html_string)
html.write_pdf(tempfile)
tempfile.seek(0)



with Image(
    file=tempfile,
    resolution=300
) as img:
    img.trim(Color('white'))
    img.format = 'png'
    img.save(filename=str(output))
