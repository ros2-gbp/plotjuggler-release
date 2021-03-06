/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

#ifndef SUGGEST_DIALOG_H
#define SUGGEST_DIALOG_H

#include <QDialog>

namespace Ui
{
class SuggestDialog;
}

class SuggestDialog : public QDialog
{
  Q_OBJECT

public:
  explicit SuggestDialog(const std::string& name_x, const std::string& name_y,
                         QWidget* parent = nullptr);
  ~SuggestDialog();

  QString nameX() const;
  QString nameY() const;
  QString suggestedName() const;

  void updateSuggestion();

private slots:
  void on_pushButtonSwap_pressed();

private:
  Ui::SuggestDialog* ui;
};

#endif  // SUGGEST_DIALOG_H
