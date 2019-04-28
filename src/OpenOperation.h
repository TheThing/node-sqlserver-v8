//---------------------------------------------------------------------------------------------------------------------------------
// File: OdbcOperation.h
// Contents: ODBC Operation objects called on background thread
// 
// Copyright Microsoft Corporation and contributors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
//
// You may obtain a copy of the License at:
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//---------------------------------------------------------------------------------------------------------------------------------

#pragma once

#include <OdbcOperation.h>

namespace mssql
{
	using namespace std;
	using namespace v8;

	class OdbcConnection;

	class OpenOperation : public OdbcOperation
	{
		wstring connectionString;
		Persistent<Object> backpointer;
		int timeout;

	public:
		OpenOperation(const shared_ptr<OdbcConnection> &connection, const wstring& connectionString,
			int timeout, Local<Object> callback, Local<Object> backpointer);
		virtual ~OpenOperation(void);
		bool TryInvokeOdbc() override;
		Local<Value> CreateCompletionArg() override;
	};
}

